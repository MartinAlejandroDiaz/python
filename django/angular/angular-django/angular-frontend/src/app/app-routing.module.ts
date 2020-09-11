import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MainComponent } from './main/main.component';

import { DepositosComponent } from './depositos/depositos.component';

import { ArticulosComponent } from './articulos/articulos.component';

import { ArticulosAddComponent } from './articulos/articulos-add/articulos-add.component';

import { DepositosAddComponent } from './depositos/depositos-add/depositos-add.component';



const routes: Routes = [
    {
        path: '',
        component: MainComponent,
        children: [
        {
            path: 'depositos',
            children: [

            {
                path: '',
                component: DepositosComponent,
            },
            {
                path: 'add',
                component: DepositosAddComponent,
            }

            ]
        },
        {
            path: 'articulos',
            children: [

            {
                path: '',
                component: ArticulosComponent,
            },
            {
                path: 'add',
                component: ArticulosAddComponent,
            }

            ]
        },
        ],
    }
];


@NgModule({
    imports: [
        RouterModule.forRoot(routes, { useHash: true }),
    ],
    exports: [
        RouterModule,
    ]
})
export class AppRoutingModule { }
export const routedComponents: any[] = [
    MainComponent,
];
