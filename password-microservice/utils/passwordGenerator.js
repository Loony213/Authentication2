const crypto = require('crypto');

class PasswordGenerator {
  static generateSecurePassword(length = 16) {
    return crypto.randomBytes(length).toString('hex'); 
  }
}

module.exports = PasswordGenerator;
