%rebase('base.tpl')
    <h1>MATRIČNI KALKULATOR</h1>
   
    Tu je seznam vaših matrik:
    <div class="float-end p-4">
    <form method="POST" action="/odjava/">
    <button type="submit" class="btn btn-outline-primary"> Odjavi se </button>
    </form>
    </div>
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
  <div class="float-end p-4">  <a href="/">Začetna stran </a> </div> <br>
     </div>
    </div>
      <form action="/operacija-ena/0/n/p/s/" method="POST">
        <select name="matrike"  class="custom-select">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit" class="btn btn-primary">Izberi operacijo </button>
      </form>