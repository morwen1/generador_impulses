import React from 'react';
import { Button, Image, StyleSheet, Text, View } from 'react-native';
import { createStackNavigator } from 'react-navigation'

import Home from './Componentes/Home/home'
import ListaNormas from './Componentes/ListaNormas/ListaNormas'
import NormaView from './Componentes/Normas/NormaView'
import CapituloView from './Componentes/Capitulo/CapituloView'


const RootStack = createStackNavigator(
  {
    Home: Home,
    ListaNormas: ListaNormas,
    NormaView: NormaView,
    CapituloView: CapituloView,
  },
  {
    initialRouteName: 'Home',
    headerMode: 'none',
  }
);


export default class App extends React.Component {
  render() {
    return <RootStack />;
  }
}
