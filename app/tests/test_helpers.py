from models.line_graph import LineGraph
from models.data_point import DataPoint
from models.vehicle_snapshot import VehicleSnapshot


def make_data_point():
    return DataPoint(10, 10)


def make_line_graph(graph_id=0):
    return LineGraph(graph_id=graph_id)


def make_two_different_data_points():
    return [DataPoint(10, 0), DataPoint(20, 10)]


def make_graph_with_two_different_data_points():
        graph = make_line_graph()
        data_points = make_two_different_data_points()
        for data_point in data_points:
            graph.add_data_point(data_point)
        return graph, data_points


def make_fully_constituted_vehicle_snapshot(vehicle_id=1, timestamp=0):
    snapshot = VehicleSnapshot(vehicle_id, timestamp)
    snapshot.acceleration = 10.0
    snapshot.velocity = 50.0
    snapshot.lane = 0
    snapshot.position = 150.0
    snapshot.desired_velocity = 60
    return snapshot