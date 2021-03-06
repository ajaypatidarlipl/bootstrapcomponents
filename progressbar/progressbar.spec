{
	"name": "bootstrapcomponents-progressbar",
	"displayName": "Progress Bar",
	"version": 1,
	"definition": "bootstrapcomponents/progressbar/progressbar.js",
	"libraries": [{"name":"bootstrapcomponents-progressbar-css", "version":"1.0", "url":"bootstrapcomponents/progressbar/progressbar.css", "mimetype":"text/css"}],
	"icon": "bootstrapcomponents/progressbar/progress_bar.png",
	"model":
	{
			"styleClass" : { "type" :"styleclass", "tags": { "scope" :"design" }, "default" : "progress-striped" , "values" :["progress-striped", "progress-striped active"]},
			"value": "float",
			"type": {"type": "string", "default":"info","values":["info", "success", "warning", "danger"]},
			"animate": {"type":"boolean", "default":true},
			"showValue" : {"type":"boolean", "default":true},
			"max" : {"type":"int", "default":100},
			"tabSeq" : {"type" :"tabseq", "tags": { "scope" :"design" }},
			"toolTipText" : { "type" : "tagstring"},
	    	"visible" : "visible"
	},
	"handlers":
	{

	},
	"api":
	{

	}

}
