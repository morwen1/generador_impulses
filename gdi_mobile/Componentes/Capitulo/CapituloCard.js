import React, { Component } from 'react'
import {
  Button,
  Image,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native'
import GlobalStyles from '../../Estilos/Comunes/GlobalStyles'
const globalStyles = GlobalStyles.createStyles()
import CardStyles from '../../Estilos/Comunes/CardStyles'
const cardStyles = CardStyles.createStyles()

class CapituloCard extends Component { 
  content() {
    const { capitulo, navigationCall } = this.props
    return (
      <TouchableOpacity
        onPress={() => navigationCall(capitulo)}
      >
        <Text style={cardStyles.CardTitleDark}>
          {capitulo.nombre}
        </Text>
      </TouchableOpacity>
    )
  }
  render() {
    return (
      <View style={cardStyles.CapitulosCard}>
        {this.content()}
      </View>
    )
  }
}

export default CapituloCard
