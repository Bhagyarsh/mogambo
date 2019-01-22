import { Component, OnInit } from '@angular/core';
import { SoftwareService } from '../../services/software.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-software-list',
  templateUrl: './software-list.component.html',
  styleUrls: ['./software-list.component.css']
})
export class SoftwareListComponent implements OnInit {

  softwareList = []

  constructor(private _softwareService: SoftwareService,
              private _router: Router) { }

  ngOnInit() {
    this._softwareService.getAll()
      .subscribe(
        res => {
          this.softwareList = res
         console.log(res)
        },
        err => {
          if (err instanceof HttpErrorResponse) {
            if (err.status === 401) {
              this._router.navigate(['/login'])
            }
          }
        })
  
      }
}
