# Separate public specs repository

Plugin-framework docs and grandMA3 platform notes lived in the same private repo. We extracted the platform notes into `grandma3-specs` so agents and other projects can share them without the Pro Plugins tree.

Skills live under `.agents/skills/` (not `.cursor/`) so Cursor, Codex, Warp, and OpenCode can discover the same folders. Interaction playbooks are skills; console facts stay in `specs/`.
