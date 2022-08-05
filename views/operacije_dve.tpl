%rebase('base.tpl')
    <div class="d-flex justify-content-between align-items-end">
    <div class="invisible"> </div>
    <div class="p-4"> <h1>MATRIČNI KALKULATOR</h1> </div>
    <div class="p-4">
    <form method="POST" action="/odjava/">
    <button type="submit" class="btn btn-outline-primary"> Odjavi se </button>
    </form>
    </div>
    </div>
    <div class="px-4"> Tu je seznam vaših matrik:</div>
    <ul>
    <div class="container ">
     <div class="row row-cols-auto">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col px-5 py-3">
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
    <div class="float-end p-4">  <a href="/">Začetna stran </a> </div> <br>
     </div>
    </div>
     <form class="p-4" action="/operacija-dve/0/n/n/" method="POST" class="container-fluid justify-content-start">
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