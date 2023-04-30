import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

function Footer() {
    return (
        <footer>
            <Container>
                <hr />
                <Row>
                    <Col className="text-center py-3">Copyright &copy; Ekmekcini</Col>
                </Row>
            </Container>
        </footer>
    )
}

export default Footer