%rebase('base.tpl')
Izberite matrike, ki jih želite odstraniti:
    <form method="POST">
    <div class="container ">
     <div class="row row-cols-4 ">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col">
      <div class="form-check">
      <input class="form-check-input" type="checkbox" name="izbrane" value="{{ id_matrike }}" id="{{ id_matrike }}">
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
    <button type="submit"> Odstrani  </button>
    </form>
    <a href="/" >Prekliči</a>