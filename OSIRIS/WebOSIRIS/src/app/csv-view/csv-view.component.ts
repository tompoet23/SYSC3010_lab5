import {Component, OnInit, ViewChild} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';

@Component({
  selector: 'app-csv-view',
  templateUrl: './csv-view.component.html',
  styleUrls: ['./csv-view.component.css']
})

export class CsvViewComponent implements OnInit {
  data: DataEntry[] = []
  displayedColumns: string[] = ['created_at', 'humid', 'press', 'temp', 'pitch', 'yaw', 'roll',  ];
  dataSource: MatTableDataSource<any>;
  length: number;

  constructor(private http: HttpClient) { }

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  ngOnInit(): void {
    this.readTextFile();

  }

  readTextFile() {
    const resultFile = this.http.get('/assets/assets/output.csv', {responseType: 'text'}).subscribe(file => {
      console.log(file);
      const csvToRowArray = file.split("\n");
      for (let index = 1; index < csvToRowArray.length; index++) {
        let row = csvToRowArray[index].split(",");
        let obj: DataEntry = {
          created_at: row[0],
          humid: row[3],
          press: row[4],
          temp: row[5],
          pitch: row[7],
          yaw: row[8],
          roll: row[8],
      }

        this.data.push(obj);
        // this.data.push(new User( parseInt( row[0], 10), row[1], row[2].trim()));
      }
      console.log(this.data);
      this.length = this.data.length;
      this.dataSource = new MatTableDataSource<any>(this.data)
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    });
    // var rawFile = new XMLHttpRequest();
    // rawFile.open('GET', 'file:\\\\C:\\Users\\plipm\\PycharmProjects\\SYSC3010_lab5\\OSIRIS\\output.csv', false);
    // rawFile.onreadystatechange( () => {
    //   if (rawFile.readyState === 4)
    //   {
    //     if (rawFile.status === 200 || rawFile.status == 0)
    //     {
    //       let allText = rawFile.responseText;
    //       alert(allText);
    //     }
    //   }
    // })
    // rawFile.send(null);
    // console.log(rawFile)
  }
}

export interface DataEntry {
  created_at;
  humid;
  press;
  temp;
  pitch;
  yaw;
  roll;
}
