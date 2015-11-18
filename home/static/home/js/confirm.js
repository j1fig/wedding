var Confirm = (function () {
    var _initialized = false;
    var _form_html;
    var _confirm_container;
    var _form_index = 0;

    var _addForm = function () {
      var form = _confirm_container
        .insert('div', ':first-child')
        .attr('id', 'form_'+_form_index)
        .classed('col-xs-4 form-container', true);
      _form_index++;

      _displayForm(form, _form_html);
    }

    var _displayForm = function (form, form_html) {
      form.html(form_html);
      $('#'+form.attr('id')+' form').on('submit', function(event) {
        event.preventDefault();
        form.select('form #submit-id-submit')
          .attr('disabled', 'disabled')
          .attr('value','Processing...')
          .classed({'processing': true});
        var core_form = '#'+form.attr('id')+' form';
        $.ajax({
          url: "/guest/add/",
          type: "POST",
          data: $(core_form).serialize(),
          success: function(data) {
            if (!(data['success'])) {
              _displayForm(d3.select(core_form), data['form_html']);
            }
            else {
              console.log(form);
              form.remove();
              d3.select('#confirmations .container-fluid')
                .classed({'confirm-success-photo': true, 'confirm-photo': false});
            }
          },
          error: function () {
            $(core_form).find('.error-message').show()
          }
        });
      });
    }

    var _bindAddAnotherGuest = function () {
      $('#add_another_guest').click( function(e){
        e.preventDefault();
        _addForm();
        return false; 
      });
    }

    var _requestGuestForm = function () {
      $.ajax({
        type: 'GET',
        url: '/guest/add/',
        success: function (data) {
          _form_html = data;
          _addForm();
        },
      })
    };

    var initialize = function () {
      _confirm_container = d3.select('.confirmations-container');
      _requestGuestForm();
      _bindAddAnotherGuest();
    }

    return {
        initialize: initialize
    }
})();

Confirm.initialize();
