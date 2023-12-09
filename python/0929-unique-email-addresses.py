class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails: set[str] = set()
        for email in emails:
            local_name, domain_name = email.split('@') #first breakage
            local_name = local_name.split('+')[0]  #preceding
            local_name = local_name.replace('.', '')
            email = local_name + '@' + domain_name #resticch ;
            unique_emails.add(email)
        return len(unique_emails)
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
tuple = (emails, emails2)
# Input: ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com'] Output: 2
# Input: ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com'] Output: 3
for item in tuple:
    print("Input:",item, "Output:", Solution().numUniqueEmails(item))