{
	"name": "bootstrapcomponents-textbox",
	"displayName": "TextBox",
	"version": 1,
	"icon": "bootstrapcomponents/textbox/textfield.png",
	"definition": "bootstrapcomponents/textbox/textbox.js",
	"serverscript": "bootstrapcomponents/textbox/textbox_server.js",
	"libraries": [{"name":"bootstrapcomponents-textbox-css", "version":"1.0", "url":"bootstrapcomponents/textbox/textbox.css", "mimetype":"text/css"}],
	"model":
	{
			"dataProviderID" : { "type":"dataprovider", "pushToServer": "allow","tags": { "scope" :"design" }, "ondatachange": { "onchange":"onDataChangeMethodID","callback":"onDataChangeCallback"}},
			"enabled" : { "type": "enabled", "blockingOn": false, "default": true, "for": ["dataProviderID","onActionMethodID","onDataChangeMethodID","onFocusGainedMethodID","onFocusLostMethodID","onRightClickMethodID"] },
			"format" : {"for":["dataProviderID"] , "type" :"format"}, 
			"inputType" : {"type":"string" , "pushToServer": "allow", "tags": { "scope" :"design", "valuesFieldType":"typeahead" }, "default" : "text",  "values" :["text", "password", "email", "tel", "date", "time", "datetime-local", "month", "week", "number", "color","search"]},			
			"readOnly" : { "type": "protected", "blockingOn": true, "default": false,"for": ["dataProviderID","onDataChangeMethodID"], "tags": {"scope":"runtime"} },
			"editable" : { "type": "protected", "blockingOn": false, "default": true,"for": ["dataProviderID","onDataChangeMethodID"] },
			"placeholderText" : "tagstring",
			"size" : {"type" :"dimension",  "default" : {"width":140, "height":20}},
			"styleClass" : { "type" :"styleclass", "tags": { "scope" :"design" }, "default": "form-control", "values" :["form-control", "input-sm"]},
			"tabSeq" : {"type" :"tabseq", "tags": { "scope" :"design" }},
			"toolTipText" : { "type" : "tagstring"},
	    	"visible" : "visible",	    
	    	"selectOnEnter" : {"type" :"boolean", "tags": { "scope" :"design" }},
	    	"autocomplete" : 
	    		{"type" :"string","tags": { "scope" :"design", "valuesFieldType":"typeahead"}, "default": "off",
	    			"values" :
	    			[ 
	    				"billing", "shipping", "home", "work", "mobile", "fax", "pager", "name", "given-name", "additional-name", "family-name","nickname", "organization-title", "username", "new-password" , "current-password", "organization", "email", "street-address", "address-level1", 
	    				"address-level2", "address-level3", "address-level4", "country", "country-name", "postal-code", "cc-name", "cc-given-name", "cc-additional-name", "cc-family-name", "cc-number", "cc-exp", "cc-exp-month", "cc-exp-year", "cc-csc", "cc-type", 
	    				"transaction-currency", "transaction-amount", "language", "bday", "bday-day", "bday-month", "bday-year", "sex", "url", "tel", "tel-country-code",  "tel-national","tel-area-code", "tel-local"
	    		    ]
	    	    }
	},
	"handlers":
	{
	         "onActionMethodID" : {

	        	"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
	        },
	        "onDataChangeMethodID" : {
	          "returns": "boolean",

	        	"parameters":[
								{
						          "name":"oldValue",
								  "type":"${dataproviderType}"
								},
								{
						          "name":"newValue",
								  "type":"${dataproviderType}"
								},
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ],
				"code": "return true"
	        },
	        "onFocusGainedMethodID" : {

	        	"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
	        },
	        "onFocusLostMethodID" : {

	        	"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
	        },
	        "onRightClickMethodID" : {

	        	"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
	        }
	},
	"api":
	{
		"requestFocus": {
				"parameters":[
						{                                                                 
						"name":"mustExecuteOnFocusGainedMethod",
						"type":"boolean",
						"optional":true
						}             
				],
				"delayUntilFormLoads": true,
				"discardPreviouslyQueuedSimilarCalls": true
	    },
	    "setInputType": {
	    	"parameters":[
						 	{
								"name":"inputType",
					 			"type":"string"
							}
						],
			"returns" : "boolean"
	   }
	}

}
