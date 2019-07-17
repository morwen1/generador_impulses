import React, {Component} from 'react'
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

class NormaCard extends Component { 
  content() {
    const { norma, navigationCall} = this.props
    return (
      <TouchableOpacity
        onPress={() => navigationCall(norma)}
      >
        <Text style={cardStyles.CardTitle}>
          {norma.descripcion}
        </Text>
      </TouchableOpacity>
    )
  }
  render() { 
    const {fullWidth } = this.props
    if (fullWidth) { 
      return (
        <View style={cardStyles.CardContainerFullWidth}>
          {this.content()}
        </View>
      ) 
    }
    
    return (
      <View style={cardStyles.CardContainer}>
        {this.content()}
      </View>
    )
  }
}

export default NormaCard
