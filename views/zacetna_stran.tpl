%rebase('base.tpl')
    <h1>Dobrodošli v matričnem kalkulatorju</h1>

    Vaše matrike:
    <ul>
    <div class="container text-center">
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
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <div class="btn-group">
        % for operacija in operacije:
          %if operacija == "potenciraj":
            <div class="input-group">
            <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2"  >
            <button type="submit" class="btn btn-info btn-md" name="operacija" value="potenciraj">Potenciraj</button>
            </div>
          %elif operacija=="mnozenje_s_skalar":
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2">  
            <button type="submit" class="btn btn-info btn-md" name="operacija" value="mnozenje_s_skalar">
            Pomnoži
            </button>
            </div>
          %else:
            <button type="submit" name="operacija" value= {{ operacija }} class="btn btn-info" >{{operacija.capitalize()}}</button>
          %end
        % end
        </div>
      </form>  
      <form action="/operacija-dveh/" method="POST">
        <select name="matrika1">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <select name="matrika2">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <div class="btn-group">
        <button type="submit" name="operacija" value="sestej" class="btn btn-info">Seštej</button>
        <button type="submit" name="operacija" value="zmnozi"class="btn btn-info">Zmnoži </button>
        </div>
      </form>