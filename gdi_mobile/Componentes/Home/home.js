import React from 'react'
import {
  Button,
  Image,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native'
import { createStackNavigator } from 'react-navigation'

import GlobalStyles from '../../Estilos/Comunes/GlobalStyles'
const globalStyles = GlobalStyles.createStyles()

class SessionManager extends React.Component {
  static navigationOptions = {
    title: 'Innova'
  };

  render() {
    const { 
      navigation
    } = this.props
    return (
      <View style={[globalStyles.fullScreenView, globalStyles.AppBackground]} >
        <View style={globalStyles.fullScreenView}>
          <Image
            style={
              globalStyles.heroImage
            }
            source={require(
            '../../Utilidades/Imagenes/fondo.jpg'
            )} />
          <View style={globalStyles.homeScrim} />
        </View>
        <View
          style={globalStyles.HomeContainer}
          >
          
          <View
          style={globalStyles.logoContainer}
          >
            <Image style={globalStyles.logoImage}
              source={require('../../Utilidades/Imagenes/innova-logo-blanco.png')}
            />
          </View>
          <Text
            style={globalStyles.heroText}
          >
            Inteligencia de agronegocios
          </Text>
          <View style={[globalStyles.accentButton,globalStyles.alignBottom]}>
            <TouchableOpacity
              onPress={() => {
                navigation.navigate('ListaNormas')
              }}
            >
              <Text
                style={globalStyles.buttonStyle}
              >Continuar</Text>
            </TouchableOpacity>
            </View>
          </View>
      </View>
    );
  }
}

export default SessionManager;
