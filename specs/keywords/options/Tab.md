---
keyword: "/Tab"
kind: option
shortcuts: ["/Ta"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_tab.html"
---

## Official

To enter the **/Tab** option keyword in the command line, use one of the options: 

  * Type **/Tab**
  * Type the shortcut**/Ta**

###  Description 

The /Tab option keyword is used to define which tab will open in the assign menu. 

###  Syntax 

**[Function] Page ["Page_Name" or Page_Number].["Executor_Name" or Executor_Number] /Tab ["Option_Value"]**

###  General Keywords 

General keywords that use the /Tab option keyword: 

  * [Assign keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html)
  * [Edit keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_edit.html)
  * [EditSetting keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_editsetting.html)
  * [Page keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_page.html)

###  Values 

The /Tab option keyword uses these values: 

  * Edit 
  * EditSetting 
  * Handle 
  * Object 

###  Examples   
  

  * To open the edit tab of executor 201 on page 1 using the assign command, type: 

```
Assign Page 1.201 /Tab "Edit"
```
---|---  
  
  * To open the assign menu and display the handle tab using the edit command, type: 

```
Edit Page 1.201 /Tab "Handle"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
