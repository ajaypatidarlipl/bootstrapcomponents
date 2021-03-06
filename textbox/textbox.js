angular.module('bootstrapcomponentsTextbox',['servoy']).directive('bootstrapcomponentsTextbox', function($formatterUtils,$svyProperties, $sabloConstants) {  
    return {
      restrict: 'E',
      scope: {
       	model: "=svyModel",
       	api: "=svyApi",
       	handlers: "=svyHandlers",
		svyServoyapi: '=svyServoyapi'
      },
      link: function($scope, $element, $attrs) {
    	  
    	  var formatState = null;
    	  var child = $element.children();
    	  var ngModel = child.controller("ngModel");
    	  
    	  $scope.model.autocomplete = $scope.model.autocomplete ? $scope.model.autocomplete : 'off';
    	  
    	  if($scope.model.inputType == "text" || $scope.model.inputType == 'number') {
    		  $scope.$watch('model.format', function(){
    			  if ($scope.model.format)
    			  {
    				  if (formatState)
    					  formatState($scope.model.format);
    				  else formatState = $formatterUtils.createFormatState(child, $scope, ngModel,true,$scope.model.format);
    			  }	  
    		  })
    	  }
    	  
    	  var tooltipState = null;
    	  Object.defineProperty($scope.model, $sabloConstants.modelChangeNotifier, {
    		  configurable: true,
    		  value: function(property, value) {
    			  switch (property) {
    			  case "selectOnEnter":
					if (value) $svyProperties.addSelectOnEnter($element);
					break;
    			  case "toolTipText":
    				  registerTooltip(value);
    				  break;
    			  }
			  }
    	  });
    	  
    	  function registerTooltip(value) {
    		  if (tooltipState)
				  tooltipState(value);
			  else
				  tooltipState = $svyProperties.createTooltipState($element, value);
    	  }
    	  
    	  var destroyListenerUnreg = $scope.$on("$destroy", function() {
    		  destroyListenerUnreg();
    		  delete $scope.model[$sabloConstants.modelChangeNotifier];
    	  });
    	  // data can already be here, if so call the modelChange function so
    	  // that it is initialized correctly.
    	  var modelChangFunction = $scope.model[$sabloConstants.modelChangeNotifier];
    	  for (key in $scope.model) {
    		  modelChangFunction(key, $scope.model[key]);
    	  }

    	  /**
    	   * Request the focus to this text field.
    	   * @example %%prefix%%%%elementName%%.requestFocus();
		   * @param mustExecuteOnFocusGainedMethod (optional) if false will not execute the onFocusGained method; the default value is true
    	   */
    	  $scope.api.requestFocus = function(mustExecuteOnFocusGainedMethod) { 
			  var inputEl = $element.find('input');
			  
			  if (mustExecuteOnFocusGainedMethod === false && $scope.handlers.onFocusGainedMethodID)
			  {
				inputEl.unbind('focus');
				inputEl[0].focus();
				inputEl.bind('focus', $scope.handlers.onFocusGainedMethodID)
			  }
			  else
			  {
				inputEl[0].focus();
			  }			  
    	  }
		 var storedTooltip = false;
		 // fill in the api defined in the spec file

		 $scope.api.onDataChangeCallback = function(event, returnval) {
			 var stringValue = typeof returnval == 'string'
				if(returnval === false || stringValue) {
					$element[0].focus();
					ngModel.$setValidity("", false);
					if (stringValue) {
						if ( storedTooltip == false)
							storedTooltip = $scope.model.toolTipText;
						registerTooltip(returnval);
					}
				}
				else {
					ngModel.$setValidity("", true);
					if (storedTooltip !== false) $scope.model.toolTipText = storedTooltip;
					storedTooltip = false;
					registerTooltip($scope.model.toolTipText );
				}
		}

    	  /**
    	   * Reset the dataProvider to null and change the inputType of the textbox.<br/>
    	   * <b>Note:</b> the value of the dataProvider bound to this field will be automatically set to null
    	   * @param {String} inputType allowed values for inputType are <i>text, tel, date, time, datetime-local, month, week, number, color</i>
    	   * @example %%prefix%%%%elementName%%.inputType("tel");
    	   */
    	  $scope.api.setInputType = function(inputType) {
    		  var types = ["text", "tel", "date", "time", "datetime-local", "month", "week", "number", "color"];

    		  if (types.indexOf(inputType) > -1) {
    			  $scope.model.dataProviderID = null;
    			  $scope.model.inputType = inputType;
    			  $scope.svyServoyapi.apply('dataProviderID');
    			  $scope.svyServoyapi.apply('inputType');
    			  return true;
    		  } else {
    			  return false;
    		  }
    	  }
      },
      templateUrl: 'bootstrapcomponents/textbox/textbox.html'
    };
  })
  
  
  
