#!/usr/bin/env node
/**
 * Send one grandMA3 command over UDP OSC to /gma3/cmd.
 * No npm dependencies (Node dgram + a minimal OSC 1.0 string message).
 *
 * Usage:
 *   node ma3-cmd.js "ReloadUI /nc"
 *   node ma3-cmd.js "DumpLog /nc" --host 127.0.0.1 --port 8000
 */

'use strict'

const dgram = require('dgram')

function printUsage() {
    process.stdout.write(
        [
            'Usage:',
            '  node ma3-cmd.js "<MA3 command>" [--host 127.0.0.1] [--port 8000]',
            '',
            'Examples:',
            '  node ma3-cmd.js "DumpLog /nc"',
            '  node ma3-cmd.js "ReloadUI /nc"',
            '  node ma3-cmd.js \'Import Plugin Library "MyPlugin.xml" At Plugin "" /o\'',
            '  node ma3-cmd.js \'Lua "Echo([[smoke_test]])"\'',
            '',
        ].join('\n')
    )
}

function parseArgs(argv) {
    const options = {
        host: '127.0.0.1',
        port: 8000,
        showHelp: false,
        command: undefined,
    }
    const positionals = []
    let i = 0
    while (i < argv.length) {
        const arg = argv[i]
        if (arg === '--help' || arg === '-h') {
            options.showHelp = true
            i += 1
            continue
        }
        if (arg === '--host') {
            const value = argv[i + 1]
            if (value === undefined || value.startsWith('-')) {
                throw new Error('Missing value for --host')
            }
            options.host = value
            i += 2
            continue
        }
        if (arg === '--port') {
            const value = argv[i + 1]
            if (value === undefined || value.startsWith('-')) {
                throw new Error('Missing value for --port')
            }
            const parsed = Number(value)
            if (!Number.isInteger(parsed) || parsed <= 0 || parsed > 65535) {
                throw new Error(`Invalid --port value: "${value}"`)
            }
            options.port = parsed
            i += 2
            continue
        }
        positionals.push(arg)
        i += 1
    }
    if (positionals.length > 0) {
        options.command = positionals.join(' ')
    }
    return options
}

function oscPaddedString(s) {
    const withNul = Buffer.from(s + '\0', 'utf8')
    const pad = (4 - (withNul.length % 4)) % 4
    return pad === 0 ? withNul : Buffer.concat([withNul, Buffer.alloc(pad)])
}

/** OSC 1.0 message: /cmd ,s <command> (grandMA3 command input). */
function encodeOscCmd(command) {
    return Buffer.concat([oscPaddedString('/cmd'), oscPaddedString(',s'), oscPaddedString(command)])
}

function sendMa3Command(options) {
    return new Promise((resolve, reject) => {
        const command = options.command
        if (command === undefined || command.trim().length === 0) {
            reject(new Error('Missing MA3 command string'))
            return
        }
        const packet = encodeOscCmd(command)
        const socket = dgram.createSocket('udp4')
        socket.send(packet, options.port, options.host, (error) => {
            socket.close()
            if (error) {
                reject(error)
                return
            }
            process.stdout.write(
                `Sent OSC command to ${options.host}:${options.port} -> ${command}\n`
            )
            resolve()
        })
    })
}

async function main() {
    try {
        const options = parseArgs(process.argv.slice(2))
        if (options.showHelp) {
            printUsage()
            return
        }
        await sendMa3Command(options)
    } catch (error) {
        const message = error instanceof Error ? error.message : String(error)
        process.stderr.write(`[ma3-cmd] ${message}\n`)
        printUsage()
        process.exitCode = 1
    }
}

void main()
