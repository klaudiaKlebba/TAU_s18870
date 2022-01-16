import org.joda.time.LocalDate;
import org.joda.time.format.DateTimeFormat;
import org.joda.time.format.DateTimeFormatter;

public class Time {
    public String ActualDate(){

        LocalDate date = LocalDate.now();
        DateTimeFormatter fmt = DateTimeFormat.forPattern("yyyy/MM/dd");
        String str = date.toString(fmt);

        return str;
    }

}
