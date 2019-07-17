import React from 'react'
import { Button, StyleSheet, Text, View } from 'react-native'
import { createStackNavigator } from 'react-navigation'

import GlobalStyles from '../../Estilos/Comunes/GlobalStyles'


class Norma extends React.Component {
  constructor(){
    super()

    this.state = {
      listaCap: [
        {id: 1},
        {id: 2},
        {id: 3},
        {id: 4}
      ]
    }

    this.listarCapitulos = this.listarCapitulos.bind(this)
  }

  static navigationOptions = ({ navigation, navigationOptions }) => {
    const { params } = navigation.state;

    return {
      title: params ? params.nombre : 'Norma',
      /* These values are used instead of the shared configuration! */
    };
  };

  listarCapitulos (){
    return this.state.listaCap.map((cap) => {
        return (
          <Button style={GlobalStyles.mapviewComponent}
            key={cap.id}
            title={'Capitulo ' + cap.id}
            onPress={() => {this.props.navigation.navigate('Norma')
            }}
          />
        );
    });
  }

  render() {
    return (
      <View style={GlobalStyles.container}>
        {this.listarCapitulos()}
        <Button
          title="Home"
          onPress={() => this.props.navigation.navigate('Home')}
        />
      </View>
    );
  }
}

export default Norma;
