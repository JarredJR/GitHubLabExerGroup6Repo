// Models/Person.cs
using System;

namespace WpfApp.Models
{
    public class Person
    {
        public int PersonId { get; set; }
        public string LastName { get; set; }
        public string GivenName { get; set; }
        public string MiddleName { get; set; }
        public Student StudentRecord { get; set; }
    }
}

// Models/Student.cs
using System;

namespace WpfApp.Models
{
    public class Student
    {
        public string StudentNumber { get; set; }
        public string Program { get; set; }
        public int Year { get; set; }
    }
}

// DataStore.cs
using System.Linq;
using System.Collections.ObjectModel;
using WpfApp.Models;

namespace WpfApp
{
    public static class DataStore
    {
        public static ObservableCollection<Person> Persons { get; } = new ObservableCollection<Person>();
        private static int nextPersonId = 1;

        public static int GetNextPersonId() => nextPersonId++;
        public static Person GetPersonById(int id) => Persons.FirstOrDefault(p => p.PersonId == id);
        public static Person GetPersonByStudentNumber(string studentNumber) =>
            Persons.FirstOrDefault(p => p.StudentRecord?.StudentNumber == studentNumber);
    }
}

// MainWindow.xaml
/*
<Window x:Class="WpfApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:local="clr-namespace:WpfApp"
        Title="Person & Student Maintenance" Height="500" Width="800">
    <DockPanel>
        <Menu DockPanel.Dock="Top">
            <MenuItem Header="_File">
                <MenuItem Header="E_xit" Click="MenuExit_Click"/>
            </MenuItem>
            <MenuItem Header="_Person">
                <MenuItem Header="Add Person" Click="MenuAddPerson_Click"/>
                <MenuItem Header="Edit Person" Click="MenuEditPerson_Click"/>
                <MenuItem Header="Delete Person" Click="MenuDeletePerson_Click"/>
            </MenuItem>
            <MenuItem Header="_Student">
                <MenuItem Header="Add Student" Click="MenuAddStudent_Click"/>
                <MenuItem Header="Edit Student" Click="MenuEditStudent_Click"/>
                <MenuItem Header="Delete Student" Click="MenuDeleteStudent_Click"/>
            </MenuItem>
            <MenuItem Header="_View">
                <MenuItem Header="View All Records" Click="MenuViewAll_Click"/>
                <MenuItem Header="View Specific Record" Click="MenuViewSpecific_Click"/>
            </MenuItem>
        </Menu>
        <ContentControl x:Name="ContentArea" />
    </DockPanel>
</Window>
*/

// MainWindow.xaml.cs
using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using WpfApp.Models;

namespace WpfApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void MenuExit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        private void MenuAddPerson_Click(object sender, RoutedEventArgs e) => ShowAddPersonUI();
        private void MenuEditPerson_Click(object sender, RoutedEventArgs e) => ShowEditPersonUI();
        private void MenuDeletePerson_Click(object sender, RoutedEventArgs e) => ShowDeletePersonUI();
        private void MenuAddStudent_Click(object sender, RoutedEventArgs e) => ShowAddStudentUI();
        private void MenuEditStudent_Click(object sender, RoutedEventArgs e) => ShowEditStudentUI();
        private void MenuDeleteStudent_Click(object sender, RoutedEventArgs e) => ShowDeleteStudentUI();
        private void MenuViewAll_Click(object sender, RoutedEventArgs e) => ShowViewAllUI();
        private void MenuViewSpecific_Click(object sender, RoutedEventArgs e) => ShowViewSpecificUI();

        private void ClearContent() => ContentArea.Content = null;

        private void ShowAddPersonUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Last Name:" });
            var txtLast = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtLast);

            panel.Children.Add(new TextBlock { Text = "Given Name:" });
            var txtGiven = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtGiven);

            panel.Children.Add(new TextBlock { Text = "Middle Name:" });
            var txtMiddle = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtMiddle);

            var btnSave = new Button { Content = "Save", Width = 100 };
            btnSave.Click += (s, e) =>
            {
                var person = new Person
                {
                    PersonId = DataStore.GetNextPersonId(),
                    LastName = txtLast.Text,
                    GivenName = txtGiven.Text,
                    MiddleName = txtMiddle.Text
                };
                DataStore.Persons.Add(person);
                MessageBox.Show($"Person added with ID {person.PersonId}");
                ClearContent();
            };
            panel.Children.Add(btnSave);

            ContentArea.Content = panel;
        }

        private void ShowEditPersonUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Enter Person ID to edit:" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);

            var btnFetch = new Button { Content = "Fetch", Width = 100 };
            btnFetch.Click += (s, e) =>
            {
                if (int.TryParse(txtId.Text, out int id))
                {
                    var person = DataStore.GetPersonById(id);
                    if (person != null)
                        ShowEditPersonDetailsUI(person);
                    else
                        MessageBox.Show("Person not found");
                }
                else MessageBox.Show("Invalid ID");
            };
            panel.Children.Add(btnFetch);

            ContentArea.Content = panel;
        }

        private void ShowEditPersonDetailsUI(Person person)
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = $"Editing Person (ID {person.PersonId})" });

            panel.Children.Add(new TextBlock { Text = "Last Name:" });
            var txtLast = new TextBox { Text = person.LastName, Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtLast);

            panel.Children.Add(new TextBlock { Text = "Given Name:" });
            var txtGiven = new TextBox { Text = person.GivenName, Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtGiven);

            panel.Children.Add(new TextBlock { Text = "Middle Name:" });
            var txtMiddle = new TextBox { Text = person.MiddleName, Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtMiddle);

            var btnSave = new Button { Content = "Save", Width = 100 };
            btnSave.Click += (s, e) =>
            {
                person.LastName = txtLast.Text;
                person.GivenName = txtGiven.Text;
                person.MiddleName = txtMiddle.Text;
                MessageBox.Show("Person record updated");
                ClearContent();
            };
            panel.Children.Add(btnSave);

            ContentArea.Content = panel;
        }

        private void ShowDeletePersonUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Enter Person ID to delete:" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);

            var btnDel = new Button { Content = "Delete", Width = 100 };
            btnDel.Click += (s, e) =>
            {
                if (int.TryParse(txtId.Text, out int id))
                {
                    var person = DataStore.GetPersonById(id);
                    if (person != null)
                    {
                        DataStore.Persons.Remove(person);
                        MessageBox.Show("Person deleted");
                        ClearContent();
                    }
                    else MessageBox.Show("Person not found");
                }
                else MessageBox.Show("Invalid ID");
            };
            panel.Children.Add(btnDel);

            ContentArea.Content = panel;
        }

        private void ShowAddStudentUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Enter Person ID to add student record:" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);

            var btnFetch = new Button { Content = "Fetch", Width = 100 };
            btnFetch.Click += (s, e) =>
            {
                if (int.TryParse(txtId.Text, out int id))
                {
                    var person = DataStore.GetPersonById(id);
                    if (person != null)
                        ShowAddStudentDetailsUI(person);
                    else MessageBox.Show("Person not found");
                }
                else MessageBox.Show("Invalid ID");
            };
            panel.Children.Add(btnFetch);

            ContentArea.Content = panel;
        }

        private void ShowAddStudentDetailsUI(Person person)
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = $"Adding student for {person.GivenName} {person.LastName} (ID {person.PersonId})" });

            panel.Children.Add(new TextBlock { Text = "Student Number:" });
            var txtNum = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtNum);

            panel.Children.Add(new TextBlock { Text = "Program:" });
            var txtProg = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtProg);

            panel.Children.Add(new TextBlock { Text = "Year:" });
            var txtYear = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtYear);

            var btnSave = new Button { Content = "Save", Width = 100 };
            btnSave.Click += (s, e) =>
            {
                if (int.TryParse(txtYear.Text, out int year))
                {
                    person.StudentRecord = new Student
                    {
                        StudentNumber = txtNum.Text,
                        Program = txtProg.Text,
                        Year = year
                    };
                    MessageBox.Show("Student record added");
                    ClearContent();
                }
                else MessageBox.Show("Invalid year");
            };
            panel.Children.Add(btnSave);

            ContentArea.Content = panel;
        }

        private void ShowEditStudentUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Enter Person ID to edit student record:" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);

            var btnFetch = new Button { Content = "Fetch", Width = 100 };
            btnFetch.Click += (s, e) =>
            {
                if (int.TryParse(txtId.Text, out int id))
                {
                    var person = DataStore.GetPersonById(id);
                    if (person != null && person.StudentRecord != null)
                        ShowEditStudentDetailsUI(person);
                    else MessageBox.Show("Student record not found");
                }
                else MessageBox.Show("Invalid ID");
            };
            panel.Children.Add(btnFetch);

            ContentArea.Content = panel;
        }

        private void ShowEditStudentDetailsUI(Person person)
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = $"Editing student for ID {person.PersonId}" });

            panel.Children.Add(new TextBlock { Text = "Student Number:" });
            var txtNum = new TextBox { Text = person.StudentRecord.StudentNumber, Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtNum);

            panel.Children.Add(new TextBlock { Text = "Program:" });
            var txtProg = new TextBox { Text = person.StudentRecord.Program, Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtProg);

            panel.Children.Add(new TextBlock { Text = "Year:" });
            var txtYear = new TextBox { Text = person.StudentRecord.Year.ToString(), Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtYear);

            var btnSave = new Button { Content = "Save", Width = 100 };
            btnSave.Click += (s, e) =>
            {
                if (int.TryParse(txtYear.Text, out int year))
                {
                    person.StudentRecord.StudentNumber = txtNum.Text;
                    person.StudentRecord.Program = txtProg.Text;
                    person.StudentRecord.Year = year;
                    MessageBox.Show("Student record updated");
                    ClearContent();
                }
                else MessageBox.Show("Invalid year");
            };
            panel.Children.Add(btnSave);

            ContentArea.Content = panel;
        }

        private void ShowDeleteStudentUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Enter Person ID to delete student record:" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);

            var btnDel = new Button { Content = "Delete", Width = 100 };
            btnDel.Click += (s, e) =>
            {
                if (int.TryParse(txtId.Text, out int id))
                {
                    var person = DataStore.GetPersonById(id);
                    if (person != null && person.StudentRecord != null)
                    {
                        person.StudentRecord = null;
                        MessageBox.Show("Student record deleted");
                        ClearContent();
                    }
                    else MessageBox.Show("Student record not found");
                }
                else MessageBox.Show("Invalid ID");
            };
            panel.Children.Add(btnDel);

            ContentArea.Content = panel;
        }

        private void ShowViewAllUI()
        {
            var grid = new DataGrid { Margin = new Thickness(10), AutoGenerateColumns = false, IsReadOnly = true };
            grid.Columns.Add(new DataGridTextColumn { Header = "ID", Binding = new Binding("PersonId") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Last Name", Binding = new Binding("LastName") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Given Name", Binding = new Binding("GivenName") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Middle Name", Binding = new Binding("MiddleName") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Student #", Binding = new Binding("StudentRecord.StudentNumber") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Program", Binding = new Binding("StudentRecord.Program") });
            grid.Columns.Add(new DataGridTextColumn { Header = "Year", Binding = new Binding("StudentRecord.Year") });
            grid.ItemsSource = DataStore.Persons;
            ContentArea.Content = grid;
        }

        private void ShowViewSpecificUI()
        {
            var panel = new StackPanel { Margin = new Thickness(20) };
            panel.Children.Add(new TextBlock { Text = "Search by Person ID (leave blank if using Student Number):" });
            var txtId = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtId);
            panel.Children.Add(new TextBlock { Text = "Search by Student Number (leave blank if using Person ID):" });
            var txtNum = new TextBox { Margin = new Thickness(0, 0, 0, 10) };
            panel.Children.Add(txtNum);

            var btnSearch = new Button { Content = "Search", Width = 100 };
            btnSearch.Click += (s, e) =>
            {
                Person person = null;
                if (int.TryParse(txtId.Text, out int id))
                    person = DataStore.GetPersonById(id);
                else if (!string.IsNullOrWhiteSpace(txtNum.Text))
                    person = DataStore.GetPersonByStudentNumber(txtNum.Text);

                if (person != null)
                    ShowPersonDetailUI(person);
                else
                    MessageBox.Show("Record not found");
            };
            panel.Children.Add(btnSearch);

            ContentArea.Content = panel;
        }

        private void ShowPersonDetailUI(Person person)
        {
            var grid = new Grid { Margin = new Thickness(20) };
            grid.ColumnDefinitions.Add(new ColumnDefinition { Width = new GridLength(150) });
            grid.ColumnDefinitions.Add(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });

            var values = new (string Label, string Value)[]
            {
                ("Person ID", person.PersonId.ToString()),
                ("Last Name", person.LastName),
                ("Given Name", person.GivenName),
                ("Middle Name", person.MiddleName),
                ("Student #", person.StudentRecord?.StudentNumber ?? string.Empty),
                ("Program", person.StudentRecord?.Program ?? string.Empty),
                ("Year", person.StudentRecord?.Year.ToString() ?? string.Empty)
            }; 

            for (int i = 0; i < values.Length; i++)
            {
                grid.RowDefinitions.Add(new RowDefinition { Height = GridLength.Auto });
                var lbl = new TextBlock { Text = values[i].Label + ":", FontWeight = FontWeights.Bold };
                Grid.SetRow(lbl, i);
                Grid.SetColumn(lbl, 0);
                var val = new TextBlock { Text = values[i].Value };
                Grid.SetRow(val, i);
                Grid.SetColumn(val, 1);
                grid.Children.Add(lbl);
                grid.Children.Add(val);
            }

            ContentArea.Content = grid;
        }
    }
}
