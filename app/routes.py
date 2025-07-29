from flask import request, jsonify
from . import app, db
from .models import MathRequest, MathRequestSchema
from .controllers import pow_op, fibonacci, factorial


@app.route('/api/pow', methods=['POST'])
def pow_route():
    data = request.get_json()
    base = data.get('base')
    exp = data.get('exp')
    result = pow_op(base, exp)
    req = MathRequest(
        operation='pow',
        input=f'{base},{exp}',
        result=str(result)
    )
    db.session.add(req)
    db.session.commit()
    return jsonify(MathRequestSchema.from_orm(req).dict())


@app.route('/api/fibonacci', methods=['POST'])
def fibonacci_route():
    data = request.get_json()
    n = data.get('n')
    result = fibonacci(n)
    req = MathRequest(
        operation='fibonacci',
        input=str(n),
        result=str(result)
    )
    db.session.add(req)
    db.session.commit()
    return jsonify(MathRequestSchema.from_orm(req).dict())


@app.route('/api/factorial', methods=['POST'])
def factorial_route():
    data = request.get_json()
    n = data.get('n')
    result = factorial(n)
    req = MathRequest(
        operation='factorial',
        input=str(n),
        result=str(result)
    )
    db.session.add(req)
    db.session.commit()
    return jsonify(MathRequestSchema.from_orm(req).dict())


@app.route('/api/history', methods=['GET'])
def history_route():
    reqs = MathRequest.query.order_by(MathRequest.timestamp.desc()).all()
    return jsonify([MathRequestSchema.from_orm(r).dict() for r in reqs])
