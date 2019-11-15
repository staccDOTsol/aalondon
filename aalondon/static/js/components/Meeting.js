import React from 'react';
import PropTypes from 'prop-types';
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'







const Meeting = props => {
  const { code = null, title = null, time = null, day = null, slug = null, postcode = null, dayRank = null } = props.meeting || {};
  let weekdayRow;
  weekdayRow = <Row>{props.day}</Row>
  return (
   
    <Row>
      <Col xs={6} md={3}><a href={'/meetings/' + props.slug}>{props.title}</a></Col>
      <Col xs={3} md={3}>{props.postcode}</Col>
      <Col xs={3} md={3}>{props.time}</Col>
    </Row>
  )
}

Meeting.propTypes = {
  title: PropTypes.string.isRequired,
  time: PropTypes.string.isRequired
};

export default Meeting;