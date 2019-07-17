import React, { Component } from 'react'
import {
  Button,
  Image,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native'
import CardStyles from '../../Estilos/Comunes/CardStyles'
const cardStyles = CardStyles.createStyles()

export default class PreguntaCard extends Component {
  render() {
    const { pregunta } = this.props
    return (
      <View style={cardStyles.PreguntasCard}>
        <Text style={cardStyles.PreguntasTitle}>
          {pregunta.descripcion}
        </Text>
      </View>
    )
  }
}
