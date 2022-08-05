%rebase('base.tpl')
Izberite matrike, ki jih želite odstraniti:
    <form method="POST">
    <div class="container ">
      <div class="row row-cols-auto">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col px-5 py-3">
      <div class="form-check">
      <input class="form-check-input" type="checkbox"  name="{{ id_matrike }}" id="{{ id_matrike }}">
      <label class="form-check-label" for="{{ id_matrike }}">   Matrika {{ id_matrike + 1 }}:
      <table class="matrika">
      % for vrstica in  matrika.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table> 
      </label>
      </div>
      </div>
    % end
    </div>
    </div>
    %if napake:
      <div class="alert alert-warning" role="alert">
                    {{ napake["izbor"] }}
       </div>
    %end
    <button type="submit" class="btn btn-secondary"> Odstrani  </button>
    </form>
    <a href="/" >Prekliči</a>