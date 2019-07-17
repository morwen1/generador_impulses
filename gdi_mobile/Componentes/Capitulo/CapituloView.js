import React, { Component } from 'react'
import {
  Button,
  Image,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
} from 'react-native'
import LayoutStyles from '../../Estilos/Components/LayoutStyles'
import PreguntaCard from '../Preguntas/PreguntaCard'
import { Icon } from 'react-native-elements'

const layoutStyles = LayoutStyles.createStyles()

export default class CapituloView extends Component {
  render() {
    const { navigation } = this.props
    const { capitulo } = navigation.state.params
    
    return (
      <ScrollView
        style={layoutStyles.ScrollView}
      >
        <View>
          <View style={layoutStyles.TransparentHeaderContainer}>
            <TouchableOpacity
              style={layoutStyles.headerFlex}
              onPress={() => navigation.goBack()}
            >
              <Icon
                name="navigate-before"
                color="#2f4770"
                iconStyle={{ paddingHorizontal: 12 }}
              />
              <Text style={layoutStyles.TitleStyles}>
                {capitulo.nombre}
              </Text>
            </TouchableOpacity>
          </View>
          {capitulo.preguntas.map((_pregunta) => {
            return (
              <PreguntaCard
                key={_pregunta.pk}
                pregunta={_pregunta}
              />
            )
          })}
        </View>
      </ScrollView>
    )
  }
}
