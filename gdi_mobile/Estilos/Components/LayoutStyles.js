import { StyleSheet, Dimensions } from 'react-native'
import {
  blanco,
  blancoTotal,
  darkGrey,
  midGrey,
  acento,
  primario,
  bodyGrey,
  bodyFontSize,
  fontSizeLarger,
  fontSizeLarge,
  fontSizeMedium,
  fontSizeSmall,
  fontSizeSmaller,
  fontSizeTiny,
  conFontSize,
  gridHeight,
  fontWeightBold,
  fontWeightLight,
  globalPaddingTiny,
  globalPaddingSmall,
  globalPadding,
  globalPaddingMedium,
  globalPaddingLarge,
  globalPaddingLarger,
  globalPaddingJumbo,
} from '../Comunes/vars'

export const fullWidth = Dimensions.get('window').width
export const fullHeight = Dimensions.get('window').height

const LayoutStyles = {
  HeaderContainer: {
    alignItems: 'flex-start',
    justifyContent: 'flex-end',
    height: 90,
    backgroundColor: blancoTotal,
    width: '100%',
    shadowOffset: {
      width: 0,
      height: 0,
    },
    shadowColor: darkGrey ,
    shadowOpacity: 0.1,
    padding: globalPadding,
  },
  TransparentHeaderContainer: {
    alignItems: 'flex-start',
    justifyContent: 'center',
    flex: 3,
    width: '100%',
    padding: globalPadding,
    top: 32,
    marginBottom:32,
  },
  FooterContainer: {
    alignContent: 'center',
    justifyContent: 'center',
    height: 64,
    width: '100%',
    shadowOffset: {
      width: 0,
      height: 0,
    },
    backgroundColor: blancoTotal,
    shadowColor: darkGrey,
    shadowOpacity: 0.1,
    position: 'absolute',
    bottom: 0,
    flexDirection: 'row',
  },
  iconStyle: {
    paddingHorizontal: globalPaddingLarge,
  },
  TitleStyles: {
    fontSize: fontSizeMedium,
    fontWeight: "800",
    color: darkGrey,
  },
  headerFlex: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'center',
  },
  scrollView: {

  },
  ScrollViewFlexWrap: {
    flex: 1,
    padding: globalPaddingSmall,
    flexDirection: 'row',
    flexWrap: 'wrap',
    alignContent: 'flex-start',
    justifyContent: 'center',
    
  },
  fullScreenView: {
    height: fullHeight,
    width: fullWidth,
  },
}

function createStyles(overrides = {}) {
  return StyleSheet.create({ ...LayoutStyles, ...overrides })
}
export default {
  createStyles,
}
