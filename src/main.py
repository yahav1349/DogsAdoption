from df_automation.dogs_adoption_df import Adoption_Dogs_df

def create_df():
    df = Adoption_Dogs_df().create_df()

def main():
    """
    Main function to retrieve and display coach and player information.
    """
    df = create_df()

if __name__ == '__main__':
    main()