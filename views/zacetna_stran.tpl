%rebase('base.tpl')
    <h1>Dobrodošli v matričnem kalkulatorju</h1>

    Vaše matrike:
    <ul>
    % for id_matrike, matrika in enumerate(matrike):
      <li>
      Matrika {{ id_matrike + 1 }}:
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
    % end
    </ul>
      Transponiraj:
      <form action="/transponiraj/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit">Transponiraj</button>
      </form>
      Izračunaj prirejenko:
      <form action="/prirejenka/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit">Prirejenka</button>
      </form>
      Izračunaj inverz:
      <form action="/inverz/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit">Inverz</button>
      </form>
      Izračunaj determinanto:
      <form action="/det/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit">Determinanta</button>
      </form>
      Izračunaj sled matrike:
      <form action="/sled/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <button type="submit">Sled</button>
      </form>
       Potenciraj matriko:
      <form action="/potenciraj/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <input name="stopnja_potence" placeholder="Stopnja potence">
        <button type="submit">Potenciraj</button>
      </form>
      Pomnoži matriko s skalarjem:
      <form action="/mnozenje_s_skalar/" method="POST">
        <select name="matrike">
        %for id_matrike in range(len(matrike)):
        <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
        %end
        </select>
        <input name="zeljen_skalar" placeholder="skalar">
        <button type="submit">Pomnoži</button>
      </form>
      Zmnoži:
        <form action="/zmnozi/" method="POST">
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
        <button type="submit">Zmnoži</button>
      </form>
      Seštej :
        <form action="/sestej/" method="POST">
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
        <button type="submit">Seštej</button>
        </form>