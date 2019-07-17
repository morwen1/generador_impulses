import React, { Component } from 'react'
import {
  Button,
  Image,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native'
import { Icon } from 'react-native-elements'
import GlobalStyles from '../../Estilos/Comunes/GlobalStyles'
const globalStyles = GlobalStyles.createStyles()
import LayoutStyles from '../../Estilos/Components/LayoutStyles'
const layoutStyles = LayoutStyles.createStyles()


class Layout extends Component { 
  render() { 
    return (
      <View style={[globalStyles.fullScreenView, {flex:1}]}>
        <View style={layoutStyles.HeaderContainer}>
          <View style={layoutStyles.headerFlex}>
            <Icon
              name="assignment"
              color="#2f4770"
              iconStyle={{paddingHorizontal:12}}
            />
            <Text style={layoutStyles.TitleStyles}>Normas</Text>
          </View>
        </View>
          {this.props.children}
        <View style={layoutStyles.FooterContainer}>
          <Icon
            name="class"
            color="#2936d6"
            iconStyle={layoutStyles.iconStyle}
          />
          <Icon
            name="assignment"
            color="#2936d6"
            iconStyle={layoutStyles.iconStyle}
          />
          <Icon
            name="assignment-turned-in"
            color="#2936d6"
            iconStyle={layoutStyles.iconStyle}
          />
        </View>
      </View>
    )
  }
}

export default Layout
