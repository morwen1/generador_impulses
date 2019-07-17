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
import CapituloCard from '../Capitulo/CapituloCard'
import { Icon } from 'react-native-elements'

const layoutStyles = LayoutStyles.createStyles()

class NormaView extends Component { 
  render() {
    const { navigation } = this.props
    const { norma } = navigation.state.params

    return (
      <ScrollView
        style={[layoutStyles.ScrollView, layoutStyles.fullScreenView]}
      >
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
                  {norma.descripcion}
                </Text>
              </TouchableOpacity>
            </View>
            {norma.capitulos.map((capitulo) => {
              return (
                <CapituloCard
                  key={capitulo.pk}
                  capitulo={capitulo}
                  navigationCall={
                    () => navigation.navigate('CapituloView', { capitulo: capitulo })
                  }
                />
              )
            })}
      </ScrollView>
    )
  }
}

export default NormaView
