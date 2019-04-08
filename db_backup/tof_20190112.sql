-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 11, 2019 at 10:52 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tof`
--
CREATE DATABASE IF NOT EXISTS `tof` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `tof`;

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `sensor_id` int(11) NOT NULL,
  `range_data` int(11) NOT NULL,
  `time` timestamp(6) NOT NULL DEFAULT '0000-00-00 00:00:00.000000'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `sensor_id`, `range_data`, `time`) VALUES
(26, 1, 3312, '2018-12-19 01:22:48.511409'),
(27, 2, 3312, '2018-12-19 01:22:48.578857'),
(28, 5, 3312, '2018-12-19 01:23:55.709868'),
(29, 8, 3312, '2018-12-19 01:23:55.766492'),
(30, 5, 3232, '2018-12-19 01:26:43.201850'),
(31, 8, 1123, '2018-12-19 01:26:48.203402'),
(32, 5, 2222, '2018-12-19 01:26:53.203003'),
(33, 5, 3312, '2018-12-19 01:33:53.745448'),
(34, 8, 4133, '2018-12-19 01:33:53.844053'),
(35, 5, 3312, '2018-12-19 01:35:05.245804'),
(36, 8, 4133, '2018-12-19 01:35:05.306334'),
(37, 5, 3312, '2018-12-19 01:35:36.618252'),
(38, 8, 4133, '2018-12-19 01:35:36.682687'),
(39, 5, 3312, '2018-12-19 03:36:39.599114'),
(40, 8, 4133, '2018-12-19 03:36:39.686986'),
(41, 5, 3312, '2018-12-19 03:36:53.972904'),
(42, 8, 4133, '2018-12-19 03:36:54.042213'),
(43, 5, 2212, '2018-12-19 03:50:52.981838'),
(44, 8, 1432, '2018-12-19 03:50:53.043345'),
(45, 5, 2212, '2018-12-19 03:55:18.406355'),
(46, 8, 1432, '2018-12-19 03:55:18.469814');

-- --------------------------------------------------------

--
-- Table structure for table `raspberry`
--

DROP TABLE IF EXISTS `raspberry`;
CREATE TABLE `raspberry` (
  `id` int(11) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `location` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `raspberry`
--

INSERT INTO `raspberry` (`id`, `ip`, `location`) VALUES
(1, '192.168.1.38', 'server test');

-- --------------------------------------------------------

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
CREATE TABLE `sensor` (
  `id` int(11) NOT NULL,
  `raspberry_id` int(11) NOT NULL,
  `xhut_pin` int(11) NOT NULL,
  `location` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`id`, `raspberry_id`, `xhut_pin`, `location`) VALUES
(5, 1, 1, 'server1'),
(8, 1, 2, 'server2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raspberry`
--
ALTER TABLE `raspberry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `raspberry`
--
ALTER TABLE `raspberry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
