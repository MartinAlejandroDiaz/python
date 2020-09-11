import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DepositosAddComponent } from './depositos-add.component';

describe('DepositosAddComponent', () => {
  let component: DepositosAddComponent;
  let fixture: ComponentFixture<DepositosAddComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DepositosAddComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DepositosAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
