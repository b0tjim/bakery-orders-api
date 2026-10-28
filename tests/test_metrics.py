def test_metrics_counts_requests_by_route_template(client):
    client.get("/health")
    client.get("/orders/999999")

    body = client.get("/metrics").text

    assert 'http_requests_total{method="GET",path="/health",status="200"}' in body
    assert 'path="/orders/{order_id}"' in body
    assert "http_request_duration_seconds_bucket" in body
