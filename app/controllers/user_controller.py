from flask import request, jsonify
from flask_login import current_user
from app.models.user_model import User
from flask_login import logout_user, login_user
from app import bcrypt


def edit_profile():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    current_user.update_profile(username, email)
    return jsonify({'message': 'Profile updated successfully'}), 200

def upload_profile_picture():
    file = request.files['file']
    if current_user.upload_profile_picture(file):
        return jsonify({'message': 'Profile picture uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Failed to upload profile picture. Check AWS credentials.'}), 500

def upload_banner_picture():
    file = request.files['file']
    if current_user.upload_banner_picture(file):
        return jsonify({'message': 'Banner picture uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Failed to upload banner picture. Check AWS credentials.'}), 500

def delete_profile_picture():
    if current_user.delete_profile_picture():
        return jsonify({'message': 'Profile picture deleted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to delete profile picture. Check AWS credentials.'}), 500

def delete_banner_picture():
    if current_user.delete_banner_picture():
        return jsonify({'message': 'Banner picture deleted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to delete banner picture. Check AWS credentials.'}), 500

def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_json()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.get_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    existing_user = User.get_user_by_email(email)
    if existing_user:
        return jsonify({'error': 'User with this email already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(username=username, email=email, password=hashed_password)
    new_user.save()

    return jsonify({'message': 'Signup successful'}), 201

def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

def delete_account():
    current_user.delete_account()
    return jsonify({'message': 'Account deleted successfully'}), 200

def send_verification_email():
    data = request.json
    email = data.get('email')

    user = User.get_user_by_email(email)
    if user:
        token = user.generate_verification_token()
        user.save()  # Save the user with updated verification token
        user.send_verification_email()
        return jsonify({'message': 'Verification email sent successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def verify_email(token):
    user = User.get_user_by_verification_token(token)
    if user:
        if user.verify_email(token):
            return jsonify({'message': 'Email verified successfully'}), 200
        else:
            return jsonify({'error': 'Invalid verification token'}), 400
    else:
        return jsonify({'error': 'User not found'}), 404

def request_password_reset():
    data = request.json
    email = data.get('email')

    user = User.get_user_by_email(email)
    if user:
        user.request_password_reset()
        return jsonify({'message': 'Password reset email sent successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('new_password')

    user = User.get_user_by_reset_password_token(token)
    if user:
        if user.reset_password(token, new_password):
            return jsonify({'message': 'Password reset successfully'}), 200
        else:
            return jsonify({'error': 'Invalid or expired reset password token'}), 400
    else:
        return jsonify({'error': 'User not found'}), 404
