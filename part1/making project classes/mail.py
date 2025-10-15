class MailClient:
	def __init__(self, server, user):
		self.data = {server: {user: []}}
		self.server = server
		self.user = user

	def receive_mail(self):
		return self.data[self.server][self.user]

	def send_mail(self, server1, user1, message):
		if server1 not in list(self.data.keys()):
			self.data[server1] = {user1: [message]}
		else:
			self.data[server1][user1].append(message)


class main:
	print('|-------------------------|')
	print('|_____MailClient v0.1_____|')
	print('|-------------------------|')
	print()
	sr = input('Enter a server: ')
	ur = input('Enter an user: ')
	cl = MailClient(sr, ur)
	while True:
		print('What you want to do?')
		print('1) Receive a mail')
		print('2) Send a mail')
		print('3) Exit')
		x = int(input('Enter a number: '))
		print()
		if x == 1:
			if cl.receive_mail() != []:
				c = 0
				for i in cl.receive_mail():
					c += 1
					print(f'{c} - message: {i}')
			else:
				print('You do not have any mails!')
		elif x == 2:
			cl.send_mail(input('Enter a server: '), input('Enter an user: '), input('Enter your message: '))
			print('Message was sent!')
		elif x == 3:
			break
		else:
			print('Wrong command!')
		print()
		print('------------------------')


if __name__ == '__main__':
	main()