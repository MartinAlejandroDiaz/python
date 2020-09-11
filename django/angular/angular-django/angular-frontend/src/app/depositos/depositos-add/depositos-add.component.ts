import { Component, OnInit } from '@angular/core';

import { Deposito } from '../../dataservice/deposito';
import { dataService } from '../../dataservice/data.service';
import { Router } from '@angular/router';




@Component({
  selector: 'app-depositos-add',
  templateUrl: './depositos-add.component.html',
  styleUrls: ['./depositos-add.component.css']
})
export class DepositosAddComponent implements OnInit {

	deposito = new Deposito();

	constructor(	private dataService: dataService,
  					private router: Router) { }

	save(): void {
		this.dataService.createDeposito(this.deposito)
		.then(
			() => this.redirect(),
			() => console.log("Error"),
		)

	}

	redirect(){
		this.router.navigate(['./depositos'])
	}

	ngOnInit() {
	}

}
