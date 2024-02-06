class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        # Initialize a set to store unique processed email addresses
        unique_emails: set[str] = set()

        # Iterate over each email in the provided list
        for email in emails:
            # Split the email into local and domain parts at the '@' symbol
            local_name, domain_name = email.split('@')  # Split email address

            # Take only the part of the local name before the first '+' symbol
            local_name = local_name.split('+')[0]  # Ignore everything after '+'

            # Remove all periods '.' from the local name
            local_name = local_name.replace('.', '')  # Remove periods

            # Reconstruct the email address with the processed local name
            email = local_name + '@' + domain_name  # Combine local and domain names

            # Add the processed email address to the set of unique emails
            unique_emails.add(email)  # Add to set

        # Optionally print the set of unique email addresses for verification
        print("uniqueEmail", unique_emails)

        # Return the number of unique email addresses
        return len(unique_emails)


# Example email lists
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
tuple = (emails, emails2)

# Iterate over each list in the tuple and print the input and output
for item in tuple:
    print("Input:", item, "Output:", Solution().numUniqueEmails(item))



