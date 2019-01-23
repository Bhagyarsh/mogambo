import { Component, OnInit } from '@angular/core';
import { SoftwareService } from '../../services/software.service';

@Component({
  selector: 'app-create-software',
  templateUrl: './create-software.component.html',
  styleUrls: ['./create-software.component.css']
})
export class CreateSoftwareComponent implements OnInit {

  softwareData = {}

  constructor(private _softwareService: SoftwareService) { }

  ngOnInit() {
  }

  addSoftware() {
  //  console.log(this.softwareData)
    this._softwareService.create(this.softwareData)
      .subscribe(
        res => {
          console.log(res)
        },
        err => console.log(err)
      )
  }

}
