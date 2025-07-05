const PasswordGenerator = require('../utils/passwordGenerator');

class PasswordService {
  static generatePassword() {
    return PasswordGenerator.generateSecurePassword();
  }
}

module.exports = PasswordService;
