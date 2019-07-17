import React from 'react'
import base64 from 'base-64'
import { 
  ScrollView,
  View,
} from 'react-native'
import Layout from '../Layout/Layout'
import NormaCard from '../Normas/NormaCard'
import LayoutStyles from '../../Estilos/Components/LayoutStyles'

const layoutStyles = LayoutStyles.createStyles()


class ListaNormas extends React.Component {
  constructor(props){
    super(props)

    this.state = {
      listaNormas: []
    }
  }
  componentDidMount() {
    //let headers = new Headers()
    //headers.append("Authorization", "Basic " + base64.encode("admin:admin"))
    //headers.append('Cache-Control', 'no-cache')
    fetch(
      'http://142.93.63.161/norma/?format=json',
      {
        method: 'GET',
        //headers: headers,
      }
    ).then((res) => {
      return res.ok && res.status === 200 ? res.json() : []
      }).then((res) => { 
        this.setState({
          listaNormas: res
        })
      }).catch((err) => { 
        console.log(err)
      })
  }

  static navigationOptions = {
    title: 'Normas'
  }

  listarNormas() {
    const { listaNormas } = this.state
    const { navigation} = this.props

    return listaNormas.map((norma, index) => {
        return (
          <NormaCard
            key={norma.pk}
            norma={norma}
            fullWidth={listaNormas.length % 2 > 0 && index === 0}
            navigationCall={
              (norma) => {
                navigation.navigate('NormaView', { norma: norma })
              }
            }
          />
        )
    });
  }

  render() {
    return (
      <Layout>
        <ScrollView style={layoutStyles.scrollView}>
          <View style={layoutStyles.ScrollViewFlexWrap}>
            {this.listarNormas()}
          </View>
        </ScrollView>
      </Layout>
    );
  }
}

export default ListaNormas;
