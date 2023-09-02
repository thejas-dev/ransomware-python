<div align="center">
  <img src="https://clarksville.computer/wp-content/uploads/2019/11/ransomware-social-980x601.png" width="50%" style="margin: auto;" alt="Malware Attack">
</div>

# Project Name

🔐 Ransomware using python

## Project Description

In the world of digital connectivity, safeguarding your data is paramount. This project is dedicated to educating individuals and organizations about the ever-present threat of ransomware and equipping them with the knowledge and tools to protect their digital assets.
As part of my educational efforts, I have created a simulated ransomware written in Python for the purpose of demonstrating its mechanisms. It is essential to use this code responsibly and ethically.

## About ransomware

- [Introduction](#project-description)
- [What is Ransomware?](#what-is-ransomware)
- [How Ransomware Works](#how-ransomware-works)
- [Impact on Victims](#impact-on-victims)
- [Preventive Measures](#preventive-measures)
- [Contributions](#contributions)
- [License](#license)

## What is Ransomware?

$Ransomware$ is a form of malware that encrypts victims files or entire system, making them inaccessible. Cybercriminals behind these attacks then demand a ransom, often in cryptocurrency or cash, in exchange for the decryption key. These ransoms can range from hundreds to millions of dollars, making it a great deal for cybercriminals.

## How Ransomware Works

Ransomware enters systems through various means, such as phishing emails or malicious websites. Once inside, it encrypts files, rendering them inaccessible without a decryption key.

## Impact on Victims

A ransomware attack can result in data loss, financial costs, reputation damage, operational disruption, and legal consequences for individuals and organizations.

## Preventive Measures

To protect yourself and your data from ransomware, follow these preventive measures:

1. **Regular Backups**: Keep backups of your critical data.
2. **Software Updates**: Keep your software and OS up to date.
3. **Employee Training**: Educate your team about cybersecurity.
4. **Security Software**: Use reputable antivirus and anti-malware tools.
5. **Network Security**: Invest in robust network security measures.
6. **Email Security**: Employ email filtering and authentication.
7. **User Privilege Restrictions**: Limit user privileges to prevent lateral movement of ransomware.
8. **Incident Response Plan**: Develop a response plan for swift action.
9. **Do Not Pay the Ransom**: Experts advise against paying ransoms.
10. **Report Attacks**: Report incidents to authorities and cybersecurity agencies.

## Contributions

We welcome contributions! If you'd like to improve this guide, please fork the repository and submit a pull request.

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## To witness the live demonstration, please follow the steps outlined below:

### ⚠️ Warning ###

**Do Not Run the Ransomware Unless You Are Aware of the Impacts:**

- Running the ransomware without understanding its consequences can result in the loss of your data.
- Do not run this code on any system or files that you do not have explicit permission to use for educational purposes.

**Educational Use Only:**

- This repository is intended solely for educational purposes and to raise awareness about the risks of ransomware in the digital world.

**Responsible Use:**

- If you choose to explore the code provided here, do so responsibly and with a clear understanding of the potential risks.

By proceeding to clone or use this repository, you acknowledge and agree to use the code responsibly and only for educational purposes. The project maintainers and contributors are not responsible for any misuse or damages that may result from using this code.

**Please use your knowledge to contribute positively to the field of cybersecurity and help protect against cyber threats.**


## Clone Repository

To get started with this project, follow these steps to clone the repository to your local machine:

1. **Open your terminal or command prompt.**

2. **Navigate to the directory where you want to store the project.**

    ```bash
    cd /path/to/your/desired/directory
    ```

3. **Clone the repository using Git.**

    ```bash
    git clone https://github.com/thejas-dev/ransomware-python.git
    ```

4. **Change into the project directory.**

    ```bash
    cd ransomware-python
    ```

5. **Now you can see a list of files including encrypt.py and decrypt.py using dir in windows and ls in linux!**
   
    <img width="277" alt="image" src="https://github.com/thejas-dev/ransomware-python/assets/107091644/fd659190-bd0c-41af-9567-8a327461a53e">

    Run the encrypt.py which will encrypt the text files in the project directory and save the key in the_key.key file.
   ⚠️ Once you encrypt the files you need a key and a secret message to decrypt it, the secret message is ```its_a_secret```
   
   ```bash
    python3 encrypt.py
    ```

7. **Now you can see the text files in the project directory are encrypted!**

    Run the decrypt.py which will decrypt the text files in the project directory once you enter the secret message ```its_a_secret``` with the the key in the_key.key file.
   
   ```bash
    python3 decrypt.py
    Enter the secret message from me
    its_a_secret
    ```

Happy learning! 🚀

---

Stay informed, stay protected, and help create a safer digital world for all! 💻🛡️
