var Confirm = (function () {
    var _initialized = false;
    var _form_html;

    var _initForm = function () {
      console.log(_form_html);
    }

    var _requestGuestForm = function () {
      $.ajax({
        type: 'GET',
        url: '/guest/add/',
        success: function (data) {
          _form_html = data['form_html'];
          _initForm();
        },
      })
    };

    var initialize = function () {
      _requestGuestForm();        
    }

    return {
        initialize: initialize
    }
})();

Confirm.initialize();
