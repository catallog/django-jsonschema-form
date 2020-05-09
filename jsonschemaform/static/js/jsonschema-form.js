let schemaContexts = [];

function loadSchema(ctx){
  let opts = Object.assign(ctx.options, {'schema': ctx.schema});
  let editor = new JSONEditor(document.getElementById('editor-'+ctx.id), opts);

  editor.on('change', function(){
    let strVal = JSON.stringify(editor.getValue());
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
