var schemaContexts = [];

function loadSchema(ctx){
  var opts = Object.assign(ctx.options, {'schema': ctx.schema});
  var editor = new JSONEditor(document.getElementById('editor-'+ctx.id), opts);

  editor.on('change', function(){
    var strVal = JSON.stringify(editor.getValue());
    document.getElementById(ctx.id).innerHTML = strVal;
  });
}

function bootstrap(ev){
  schemaContexts.forEach(
    function(context) {
      loadSchema(JSON.parse(context));
    }
  );
}

document.addEventListener("DOMContentLoaded", bootstrap);
