%rebase('base.tpl')
    <h1>MATRIČNI KALKULATOR</h1>
    Dobrodošli!
    Tu je seznam vaših matrik:
    <ul>
    <div class="container ">
     <div class="row row-cols-4">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col">
      <li>   Matrika {{ id_matrike + 1 }}:
      <table class="matrika">
      % for vrstica in  matrika.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table> 
      </li>
      </div>
    % end
    </ul>
    <div class="col"> <a href="/dodaj-matriko/">Dodaj matriko </a> </div>
     </div>
    </div>
     <form action="/operacija-dveh/" method="POST" class="container-fluid justify-content-start">
        <select name="matrika1" class="custom-select">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <select name="matrika2" class="custom-select">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit" class="btn btn-primary">Izberi operacijo </button>
    </form>