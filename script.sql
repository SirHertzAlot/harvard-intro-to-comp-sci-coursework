ALTER TABLE users
ADD COLUMN user_followers TEXT;
ALTER TABLE users
ADD COLUMN 
  user_follower_count INTEGER DEFAULT 0;