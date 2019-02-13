var $ = jQuery || django.jQuery;

var schemaContexts = [];


function loadSchema(ctx){
  var opts = $.extend({}, ctx.options, {'schema': ctx.schema});
  var editor = new JSONEditor(document.getElementById('editor-'+ctx.id), opts);

  editor.on('change', function(){
    var strVal = JSON.stringify(editor.getValue());
    $('#'+ctx.id).html(strVal);
  });
}

function bootstrap(ev){
  schemaContexts.forEach(
    function(context) {
      loadSchema(JSON.parse(context))
    }
  );
}

document.addEventListener("DOMContentLoaded", bootstrap);
