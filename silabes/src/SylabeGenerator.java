/**
 * Created by marodrig on 06/03/2015.
 */
public class SylabeGenerator {

    public static void main(String[] args) {

        //p t k b d g f T (th) s S (sh) v D (dh) z Z (zh) J (ch) _ (dz)
        String[] c = {"p", "t", "k", "b", "d", "g", "f", "T", "s", "sh", "v", "dh", "z", "Zh", "ch", "dz"};
        String[] v = {"a", "e", "i", "o", "u"};

        for (int j = 0; j < v.length; j++) {
            for (int i = 0; i < c.length; i++) {
                System.out.println(c[i] + v[j]);
            }
        }
    }


}
