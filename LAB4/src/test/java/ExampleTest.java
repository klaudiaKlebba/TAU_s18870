import ApacheCollections.Customer;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.Predicate;
import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

import static org.junit.Assert.*;


public class ExampleTest {

    private Add add;
    private Subtract subtract;
    private Multiply multiply;
    private Divide divide;
    private Time time;

    @Test
    public void AddPositive() {
        add = new Add();
        int result = add.add(2, 2);
        assertEquals(4,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void AddFail() {
        add = new Add();
        int result = add.add(2, 2);
        assertEquals(0,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void AddPositiveArray() {
        add = new Add();
        int[] results = {add.add(2, 2),add.add(3, 3)};
        Assert.assertArrayEquals(results,new int[] {4,6});
        System.out.println("APA :" + Arrays.toString(results));
    }

    @Test
    public void AddNegative(){
        add = new Add();
        int result = add.add(2, 2);
        Assert.assertNotEquals(5,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void SubPositive(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        assertEquals(2,result);
        System.out.println("SP :" + result);
    }

    @Test
    public void SubFail(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        assertEquals(0,result);
        System.out.println("SP :" + result);
    }

    @Test
    public void SubPositiveArray(){
        subtract = new Subtract();
        int[] results = {subtract.subtract(4, 2), subtract.subtract(6, 3)};
        Assert.assertArrayEquals(results,new int[] {2,3});
        System.out.println("SPA :" + Arrays.toString(results));
    }

    @Test
    public void SubNegative(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        Assert.assertNotEquals(4,result);
        System.out.println("SN :" + result);
    }

    @Test
    public void MulPositive(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        assertEquals(8,result);
        System.out.println("MP :" + result);
    }

    @Test
    public void MulFail(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        assertEquals(0,result);
        System.out.println("MP :" + result);
    }

    @Test
    public void MulPositiveArray(){
        multiply = new Multiply();
        int[] results = {multiply.multiply(4, 2), multiply.multiply(6, 3)};
        Assert.assertArrayEquals(results,new int[] {8,18});
        System.out.println("MPA :" + Arrays.toString(results));
    }

    @Test
    public void MulNegative(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        Assert.assertNotEquals(9,result);
        System.out.println("MN :" + result);
    }

    @Test
    public void DivPositive() {
        divide = new Divide();
        int result = divide.divide(2, 2);
        assertEquals(1,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void DivFail() {
        divide = new Divide();
        int result = divide.divide(2, 2);
        assertEquals(0,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void DivPositiveArray() {
        divide = new Divide();
        int[] results = {divide.divide(2, 2),divide.divide(4, 2)};
        Assert.assertArrayEquals(results,new int[] {1,2});
        System.out.println("APA :" + Arrays.toString(results));
    }

    @Test
    public void DivNegative(){
        divide = new Divide();
        int result = divide.divide(2, 2);
        Assert.assertNotEquals(5,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void DivZero(){
        divide = new Divide();
        int result = divide.divide(2, 0);
        assertEquals(-1,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void ActualDate(){
        // funkcja korzysta z Joda-Time porownuje wynik z wbudowanym java.time

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        LocalDateTime now = LocalDateTime.now();

        time = new Time();
        String result = time.ActualDate();

        assertEquals(dtf.format(now),result);
        System.out.println("T :" + result);
    }

    Customer customer1 = new Customer(1, "Klaudia", "locality1", "city1");
    Customer customer2 = new Customer(2, "Lukas", "locality2", "city2");
    Customer customer3 = new Customer(3, "Martyna", "locality3", "city3");
    Customer customer4 = new Customer(4, "Kamil", "locality4", "city4");
    Customer customer5 = new Customer(5, "Marek", "locality5", "city5");
    Customer customer6 = new Customer(6, "Zenek", "locality6", "city6");

    List<Customer> list1 = Arrays.asList(customer1, customer2, customer3);
    List<Customer> list2 = Arrays.asList(customer4, customer5, customer6);
    List<Customer> list3 = Arrays.asList(customer1, customer2);

    @Test
    public void NoNullAdded() {
        CollectionUtils.addIgnoreNull(list1, null);

        assertFalse(list1.contains(null));
    }

    @Test
    public void IsNotEmpty() {
        assertTrue(CollectionUtils.isNotEmpty(list2));
    }

    @Test
    public void ElementNotPresent() {
        Collection<Customer> result = CollectionUtils.subtract(list1, list3);
        assertFalse(result.contains(customer1));
    }

}
