import unittest
from Tasks.InterviewTasks.AppliedIntuitionInterview import FileSystem, are_there_bad_words, test_manual_links


class AppliedIntuitionInterviewMkdirTest(unittest.TestCase):

    # Testing string approach, implemented at the interview:
    file_system = FileSystem()

    # The following 7 tests are sequential and depend on each other's results,
    # therefore can't be run individually or in a different order
    def test_AppliedIntuitionInterviewMkdir1(self):
        given_path = "/foo"
        expected_result = "OK"
        expected_structure = {'foo': {}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir2(self):
        given_path = "/foo/bar"
        expected_result = "OK"
        expected_structure = {'foo': {'bar': {}}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir3(self):
        given_path = "/foo/bar/baz"
        expected_result = "OK"
        expected_structure = {'foo': {'bar': {'baz': {}}}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir4(self):
        given_path = "/bar"
        expected_result = "OK"
        expected_structure = {'foo': {'bar': {'baz': {}}}, 'bar': {}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir5(self):
        given_path = "/foo/bar"
        expected_result = "Error: Directory already exists!"
        expected_structure = {'foo': {'bar': {'baz': {}}}, 'bar': {}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir6(self):
        given_path = "/baz/foo"
        expected_result = "Error: No directory 'baz' found!"
        expected_structure = {'foo': {'bar': {'baz': {}}}, 'bar': {}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    def test_AppliedIntuitionInterviewMkdir7(self):
        given_path = "/foo/baz/bar"
        expected_result = "Error: No directory 'baz' found!"
        expected_structure = {'foo': {'bar': {'baz': {}}}, 'bar': {}}
        actual_result = self.file_system.mkdir(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(self.file_system.structure, expected_structure)

    # Testing graph approach:
    file_system2 = FileSystem(FileSystem().Directory("/"))

    # The following 7 tests are sequential and depend on each other's results,
    # therefore can't be run individually or in a different order
    def test_AppliedIntuitionInterviewMkdirGraphApproach1(self):
        given_path = "/foo"
        expected_result = "OK"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach2(self):
        given_path = "/foo/bar"
        expected_result = "OK"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach3(self):
        given_path = "/foo/bar/baz"
        expected_result = "OK"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'].sub_dirs['baz'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach4(self):
        given_path = "/bar"
        expected_result = "OK"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'].sub_dirs['baz'])
        self.assertTrue(self.file_system2.structure.sub_dirs['bar'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach5(self):
        given_path = "/foo/bar"
        expected_result = "Error: Directory already exists!"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'].sub_dirs['baz'])
        self.assertTrue(self.file_system2.structure.sub_dirs['bar'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach6(self):
        given_path = "/baz/foo"
        expected_result = "Error: No directory 'baz' found!"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'].sub_dirs['baz'])
        self.assertTrue(self.file_system2.structure.sub_dirs['bar'])

    def test_AppliedIntuitionInterviewMkdirGraphApproach7(self):
        given_path = "/foo/baz/bar"
        expected_result = "Error: No directory 'baz' found!"
        actual_result = self.file_system2.mkdir_graph_approach(given_path)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(self.file_system2.structure.sub_dirs['foo'].sub_dirs['bar'].sub_dirs['baz'])
        self.assertTrue(self.file_system2.structure.sub_dirs['bar'])


class AppliedIntuitionInterviewBadWordsTest(unittest.TestCase):

    bad_words = ["basically", "like"]

    def test_AppliedIntuitionInterviewBadWordsHappyPath(self):
        given_sentence = "The two approaches are very similar."
        expected_result = "The sentence has no bad words. Good job!"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsEmpty(self):
        given_sentence = ""
        expected_result = "The sentence has no bad words. Good job!"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically1(self):
        given_sentence = "The two approaches are basically very similar."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically2(self):
        given_sentence = "The two approaches are basically"
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically3(self):
        given_sentence = "The two approaches are basically."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically4(self):
        given_sentence = "basically very similar."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically5(self):
        given_sentence = "Basically very similar."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically6(self):
        given_sentence = "The two approaches are BASICALLY very similar."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsBasically7(self):
        given_sentence = "The two approaches are BaSiCaLlY very similar."
        expected_result = f"The sentence has the following bad words: 'basically'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsLike(self):
        given_sentence = "The two approaches are like very similar."
        expected_result = f"The sentence has the following bad words: 'like'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsLikeBasically(self):
        given_sentence = "The two approaches like are basically very similar."
        expected_result = f"The sentence has the following bad words: 'basically', 'like'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewBadWordsLikeBasically2(self):
        given_sentence = "The two approaches like are basically like very similar."
        expected_result = f"The sentence has the following bad words: 'basically', 'like'. Consider correcting"
        actual_result = are_there_bad_words(given_sentence, self.bad_words)
        self.assertEqual(expected_result, actual_result)


class AppliedIntuitionInterviewTestManualLinksTest(unittest.TestCase):

    MANUAL_CONTENTS = """
    # Welcome to Simian

    Simian is a tool designed to help you test autonomous vehicle stacks in simulation.

    ## Overview
    1. [Key features](#key-features)
    2. [Running simulations](#running-simulations)
    3. [Viewing results](#viewing-results)

    ## Key features

    ### Custom built for AVs

    Get deterministic results from a validated simulation engine.

    ### Easy integration

    Integrate with your AV software within weeks.

    ### Optimized for scale

    Deploy to a cloud or on-prem cluster to run millions of simulations.

    ## Modular testing of AV stack

    Simulate everything from individual modules to your full system stack.

    ### Computationally lightweight

    Run simulations on commodity servers to reduce your infrastructure investment.

    ### Open source compatibility

    Works with common open source formats for scenarios, drive data, and interface APIs.

    ## Running simulations

    Running simulations is as easy as clicking a button. Once you run a simulation, you can view a result on the [results page](#results).

    Morbi in dapibus dui, sed posuere odio. Quisque suscipit scelerisque semper. Aliquam erat volutpat. Aenean et tellus enim. Aliquam erat volutpat. Morbi ullamcorper risus id bibendum accumsan. Praesent sodales lorem efficitur urna porttitor, ut cursus turpis convallis.

    Pellentesque lacinia sapien et elit facilisis blandit. Sed eget egestas magna. Ut elementum velit at odio rutrum, sit amet mattis purus condimentum. Cras diam purus, egestas et felis eget, malesuada pulvinar est. Donec a dictum ex. Proin vestibulum porta elit in cursus. Donec luctus finibus lacinia. Donec condimentum, sem at suscipit ornare, tortor dolor dapibus justo, et tempor elit sem ac mi. Aenean laoreet feugiat efficitur. Suspendisse ipsum ex, auctor in odio a, pretium tristique ipsum. Sed convallis tortor et dui gravida rhoncus. Nam ut elit lacinia, hendrerit arcu id, pellentesque nulla.

    ## Viewing results

    Use the Simian UI to play back and inspect the results from a simulation.
    Praesent pretium, velit tempor maximus tincidunt, sem ligula lacinia lorem, sit amet sodales enim turpis sit amet lectus. Integer ac scelerisque metus, ac sodales diam. In vitae varius purus, sed aliquet ipsum. Nulla facilisi. Cras dictum dui eu consectetur molestie. Fusce porttitor eleifend dictum. Ut id lectus vel mauris cursus cursus a id elit. Praesent vulputate elit ut quam sagittis lobortis. Suspendisse potenti. Etiam congue eleifend dignissim. Integer aliquam elementum placerat. Integer facilisis convallis odio, vel cursus nisl tincidunt quis. Morbi molestie mauris posuere pretium fringilla. Sed molestie velit et tellus malesuada imperdiet. Integer ac quam fermentum, fringilla lacus eu, rutrum metus.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae luctus velit, non fermentum nisl. Suspendisse justo lorem, pretium at augue vel, gravida aliquam ligula. Nulla id sagittis purus. Etiam at arcu quis lorem fringilla lobortis. Sed posuere, velit sed convallis pulvinar, nulla nisl faucibus ipsum, maximus congue est ante et nulla. Pellentesque hendrerit magna mauris, id sodales ligula tempor ut. Mauris tempus lectus at vulputate pretium. Nullam pellentesque congue euismod. Donec porta, lectus lobortis vulputate rutrum, magna felis tincidunt nisi, vel finibus ligula leo at risus.

    For more information, check out our website at [applied.co](https://applied.co)!
    """

    MANUAL_CONTENTS_WITHOUT_ERRORS = """
    # Welcome to Simian

    Simian is a tool designed to help you test autonomous vehicle stacks in simulation.

    ## Overview
    1. [Key features](#key-features)
    2. [Running simulations](#running-simulations)
    3. [Viewing results](#viewing-results)

    ## Key features

    ### Custom built for AVs

    Get deterministic results from a validated simulation engine.

    ### Easy integration

    Integrate with your AV software within weeks.

    ### Optimized for scale

    Deploy to a cloud or on-prem cluster to run millions of simulations.

    ## Modular testing of AV stack

    Simulate everything from individual modules to your full system stack.

    ### Computationally lightweight

    Run simulations on commodity servers to reduce your infrastructure investment.

    ### Open source compatibility

    Works with common open source formats for scenarios, drive data, and interface APIs.

    ## Running simulations

    Running simulations is as easy as clicking a button. Once you run a simulation, you can view a result on the results page.

    Morbi in dapibus dui, sed posuere odio. Quisque suscipit scelerisque semper. Aliquam erat volutpat. Aenean et tellus enim. Aliquam erat volutpat. Morbi ullamcorper risus id bibendum accumsan. Praesent sodales lorem efficitur urna porttitor, ut cursus turpis convallis.

    Pellentesque lacinia sapien et elit facilisis blandit. Sed eget egestas magna. Ut elementum velit at odio rutrum, sit amet mattis purus condimentum. Cras diam purus, egestas et felis eget, malesuada pulvinar est. Donec a dictum ex. Proin vestibulum porta elit in cursus. Donec luctus finibus lacinia. Donec condimentum, sem at suscipit ornare, tortor dolor dapibus justo, et tempor elit sem ac mi. Aenean laoreet feugiat efficitur. Suspendisse ipsum ex, auctor in odio a, pretium tristique ipsum. Sed convallis tortor et dui gravida rhoncus. Nam ut elit lacinia, hendrerit arcu id, pellentesque nulla.

    ## Viewing results

    Use the Simian UI to play back and inspect the results from a simulation.
    Praesent pretium, velit tempor maximus tincidunt, sem ligula lacinia lorem, sit amet sodales enim turpis sit amet lectus. Integer ac scelerisque metus, ac sodales diam. In vitae varius purus, sed aliquet ipsum. Nulla facilisi. Cras dictum dui eu consectetur molestie. Fusce porttitor eleifend dictum. Ut id lectus vel mauris cursus cursus a id elit. Praesent vulputate elit ut quam sagittis lobortis. Suspendisse potenti. Etiam congue eleifend dignissim. Integer aliquam elementum placerat. Integer facilisis convallis odio, vel cursus nisl tincidunt quis. Morbi molestie mauris posuere pretium fringilla. Sed molestie velit et tellus malesuada imperdiet. Integer ac quam fermentum, fringilla lacus eu, rutrum metus.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae luctus velit, non fermentum nisl. Suspendisse justo lorem, pretium at augue vel, gravida aliquam ligula. Nulla id sagittis purus. Etiam at arcu quis lorem fringilla lobortis. Sed posuere, velit sed convallis pulvinar, nulla nisl faucibus ipsum, maximus congue est ante et nulla. Pellentesque hendrerit magna mauris, id sodales ligula tempor ut. Mauris tempus lectus at vulputate pretium. Nullam pellentesque congue euismod. Donec porta, lectus lobortis vulputate rutrum, magna felis tincidunt nisi, vel finibus ligula leo at risus.

    For more information, check out our website at https://applied.co!
    """

    def test_AppliedIntuitionInterviewTestManualLinksDefault(self):
        given_text = self.MANUAL_CONTENTS
        expected_result = "Warning, no heading found for: #results, https://applied.co"
        actual_result = test_manual_links(given_text)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewTestManualLinksLinkTypo(self):
        given_text = self.MANUAL_CONTENTS.replace("#running-simulations", "#runing-simulations")
        expected_result = "Warning, no heading found for: #runing-simulations, #results, https://applied.co"
        actual_result = test_manual_links(given_text)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewTestManualLinksHeadingTypo(self):
        given_text = self.MANUAL_CONTENTS.replace("## Viewing results", "## Viewin results")
        expected_result = "Warning, no heading found for: #viewing-results, #results, https://applied.co"
        actual_result = test_manual_links(given_text)
        self.assertEqual(expected_result, actual_result)

    def test_AppliedIntuitionInterviewTestManualWithoutErrors(self):
        given_text = self.MANUAL_CONTENTS_WITHOUT_ERRORS
        expected_result = "Everything looks cool"
        actual_result = test_manual_links(given_text)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
