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
    <form action="/operacija/" method="POST">
    </form>
      <form action="/operacija-ena/" method="POST">
        <select name="matrike"  class="custom-select">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <div class="container">
         <div class="row row-cols-8">
        % for operacija in operacije:
          %if operacija == "potenciraj":
          <div class="col">
            <div class="input-group">
            <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2"  >
            <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="potenciraj" >Potenciraj</button>
            </div>
          </div>
          %elif operacija=="mnozenje_s_skalar":
          <div class="col">
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2">  
            <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="mnozenje_s_skalar">
            Pomnoži
            </button>
            </div>
          </div>
          %else:
          <div class="col">
            <button type="submit" name="operacija" value= {{ operacija }} class="btn btn-outline-primary" >{{operacija.capitalize()}}</button>
          </div>
          %end
        % end
         </div>
        </div>
      </form>  
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

     
     